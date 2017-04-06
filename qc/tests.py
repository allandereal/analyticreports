from django.test import TestCase
from .models import Contact, Message


class DumpTest(TestCase):
    def test_one_plus_one(self):
        self.assertEquals(1+1, 2)


class TestContact(TestCase):

    def test_add_contacts(self):
        contact_count = Contact.objects.count()
        added_contacts = Contact.save_contacts()
        self.assertEquals(Contact.objects.count(), contact_count + added_contacts)

    def test_contact_exists(self):
        class C(object):
            def __init__(self, uuid=None, name=None, language=None, urns=None,
                         groups=None, fields=None, blocked=None, stopped=None, created_on=None, modified_on=None):
                self.uuid = uuid
                self.name = name
                self.language = language
                self.urns = urns
                self.groups = groups
                self.fields = fields
                self.blocked = blocked
                self.stopped = stopped
                self.created_on = created_on
                self.modified_on = modified_on

        qc_mock_contact = C(uuid="uuid-test", name="name-test", language="language-test", urns="urns-test",
                            groups="groups-test", fields="fields-test", blocked=False, stopped=False, created_on=None,
                            modified_on=None)
        self.assertEquals(Contact.contact_exists(qc_mock_contact), False)
        Contact.objects.create(uuid="uuid-test", name="name-test", language="language-test", urns="urns-test",
                               groups="groups-test", fields="fields-test", blocked=False, stopped=False,
                               created_on=None, modified_on=None)
        self.assertEquals(Contact.contact_exists(qc_mock_contact), True)


class TestMessage(TestCase):

    def test_add_messages(self):
        message_count = Message.objects.count()
        added_messages = Message.save_messages()
        self.assertEquals(Message.objects.count(), message_count + added_messages)

    def test_message_exists(self):
        class M(object):
            def __init__(self, id=None, broadcast=None, contact=None, urn=None, channel=None, direction=None, type=None,
                         status=None, visibility=None, text=None, labels=None, created_on=None, sent_on=None,
                         modified_on=None):
                self.id = id
                self.broadcast = broadcast
                self.contact = contact
                self.urn = urn
                self.channel = channel
                self.direction = direction
                self.type = type
                self.status = status
                self.visibility = visibility
                self.text = text
                self.labels = labels
                self.sent_on = sent_on
                self.created_on = created_on
                self.modified_on = modified_on

        qc_mock_message = M(id=1, broadcast=1, contact="contact-test", urn="urn-test", channel="channel-test",
                            direction="direction-test", type="type-test", status="status-test",
                            visibility="visibility-test", text="text-test", labels="labels-test", created_on=None,
                            sent_on=None, modified_on=None)
        self.assertEquals(Message.message_exists(qc_mock_message), False)
        Message.objects.create(id=1, broadcast=1, contact="contact-test", urn="urn-test", channel="channel-test",
                               direction="direction-test", type="type-test", status="status-test",
                               visibility="visibility-test", text="text-test", labels="labels-test", created_on=None,
                               sent_on=None, modified_on=None)
        self.assertEquals(Message.message_exists(qc_mock_message), True)
