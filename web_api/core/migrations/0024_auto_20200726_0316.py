# Generated by Django 3.0.3 on 2020-07-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_account_limit_billing_access_to_owners"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="subscription_exempt",
            field=models.BooleanField(
                default=False,
                help_text="This account does not require a subscription. Potentially a GitHub Sponsor, Enterprise subscriber, non profit, etc.",
            ),
        ),
        migrations.AddField(
            model_name="account",
            name="subscription_exempt_message",
            field=models.TextField(
                help_text="Explanation for the subscription exemption to be displayed in the Usage & Billing page.",
                null=True,
            ),
        ),
    ]
