from linodecli import cli


class LinodeDynDNS(object):
    DOMAINS_LIST_OP = cli.ops['domains']['list']
    DOMAINS_RECORD_LIST_OP = cli.ops['domains']['records-list']

    def __init__(self, pld, subdomain, my_ip, priority=10, weight=5, port=80, ttl_sec=3600):
        super(LinodeDynDNS, self).__init__()
        self._ttl_sec = ttl_sec
        self._port = port
        self._weight = weight
        self._priority = priority

        self._subdomain = subdomain
        self._my_ip = my_ip

        self._domains_list_op = cli.ops['domains']['list']
        self._domains_record_list_op = cli.ops['domains']['records-list']

        self._domain_record = self._fetch_domain_record(pld)
        self._domain_id = str(self._domain_record['id'])
        self._records = None

    @staticmethod
    def _normalize_result(result):
        return result['data'] if 'pages' in result else [result]

    @staticmethod
    def _do_cli_op(op, args):
        return LinodeDynDNS._normalize_result(cli.do_request(op, args).json())

    @classmethod
    def _fetch_domain_record(cls, private_level_domain):
        domains_list_result = cls._do_cli_op(cls.DOMAINS_LIST_OP, None)
        domain_record = next((x for x in domains_list_result if x['domain'] == private_level_domain), None)

        if not domain_record:
            raise Exception("Domain record for '{}' was not found".format(private_level_domain))

        return domain_record

    @classmethod
    def fetch_subdomain_record(cls, domain_id, subdomain):
        records = cls._do_cli_op(cls.DOMAINS_RECORD_LIST_OP, [domain_id])

        return next((rec for rec in records if rec['type'] == 'A' and rec['name'] == subdomain), None)

    def try_update(self):
        """
        :return: Record which was created/updated
        """
        subdomain_record = self.fetch_subdomain_record(self._domain_id, self._subdomain)
        update_parameters = [self._domain_id]

        operation = cli.ops['domains']['records-create']
        if subdomain_record:
            operation = cli.ops['domains']['records-update']
            update_parameters.append(str(subdomain_record['id']))

        update_parameters.append(self._create_update_parameters())
        update_parameters = ' '.join(update_parameters)

        return self._do_cli_op(operation, update_parameters.split(' '))


    def _create_update_parameters(self):
        return '--type A --name {subdomain} --target {ip} --priority {priority} --weight {weight} --port {port} ' \
               '--ttl_sec {ttl_sec}'.format(subdomain=self._subdomain, ip=self._my_ip, priority=self._priority,
                                            weight=self._weight, port=self._port, ttl_sec=self._ttl_sec)


def main():
    ldns = LinodeDynDNS('stupid.co.il', 'h', '79.179.249.228')
    ldns.try_update()


if __name__ == "__main__":
    main()
