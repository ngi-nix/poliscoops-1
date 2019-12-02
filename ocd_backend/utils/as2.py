class AS2ConverterMixin(object):
    def as2_transform_old_object(self, actual_combined_index_data):
        combined_index_data = {
            'hidden': actual_combined_index_data.get('hidden', False),
            # 'source': unicode(
            #     self.source_definition.get('source', 'Partij nieuws')),
            # 'type': unicode(self.source_definition.get('type', 'Partij')),
            # 'parties': [unicode(self.source_definition['collection'])]
        }
        loc = actual_combined_index_data.get('location', u'NL')
        party_name = unicode(actual_combined_index_data['parties'][0])
        parties = [self.get_organization(p, loc) for p in actual_combined_index_data['parties']]
        persons = [self.get_person(p, loc) for p in actual_combined_index_data['politicians']]
        content = actual_combined_index_data.get('description', None)
        pub_date = actual_combined_index_data.get('date', None)
        actual_link = actual_combined_index_data.get('link', None) or actual_combined_index_data['meta']['original_object_urls']['html']
        combined_index_data['item'] = {
            "@type": "Create",
            "created": pub_date,
            "actor": self.get_organization(
                party_name, loc),
            "object": {
                "@type": "Note",
                "name": combined_index_data.get('title', None),
                "content": content,
                "created": pub_date,
                "@id": self.get_identifier('Note', actual_link),
                "tag": parties + persons,
                "url": actual_link
            },
#            "@context": "http://www.w3.org/ns/activitystreams"
        }
        return combined_index_data
