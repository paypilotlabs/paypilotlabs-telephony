import frappe
from frappe.tests import IntegrationTestCase

from telephony import api
from telephony.exotel.handler import make_a_call
from telephony.utils import get_contact

PORTAL_USER = "tp-portal-user@example.com"


class TestDeskOnlyMethods(IntegrationTestCase):
    """Products like Helpdesk let portal users reach telephony.*; staff methods must refuse them."""

    def setUp(self):
        frappe.db.savepoint("tp_desk_only")
        if not frappe.db.exists("User", PORTAL_USER):
            frappe.get_doc(
                {
                    "doctype": "User",
                    "email": PORTAL_USER,
                    "first_name": "Portal",
                    "user_type": "Website User",
                    "send_welcome_email": 0,
                }
            ).insert(ignore_permissions=True)
        frappe.set_user(PORTAL_USER)

    def tearDown(self):
        frappe.set_user("Administrator")
        frappe.db.rollback(save_point="tp_desk_only")

    def test_portal_user_is_refused(self):
        calls = [
            lambda: api.get_call_log("CA-any"),
            lambda: api.get_contact_by_phone_number("9"),
            lambda: api.set_default_calling_medium("Twilio"),
            lambda: api.create_telephony_agent(),
            lambda: api.create_call_log(
                "CA-x", "Twilio", "1", "2", 0, "Completed", "Outgoing", None, None, []
            ),
            lambda: make_a_call("+15550000000", "+15550000001", "08000000000"),
        ]
        for call in calls:
            with self.assertRaises(frappe.PermissionError):
                call()

    def test_desk_user_rejects_unknown_medium(self):
        frappe.set_user("Administrator")
        with self.assertRaises(frappe.ValidationError):
            api.set_default_calling_medium("Skype")

    def test_contact_lookup_ignores_wildcards(self):
        frappe.set_user("Administrator")
        self.assertEqual(get_contact("%"), {"mobile_no": "%"})
