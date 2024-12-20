import logging
from typing import Any, Dict
from pathlib import Path
import emails
from emails.template import JinjaTemplate
from .. import schemas

EMAILS_ENABLED = True
SMTP_TLS = True
SMTP_PORT = 25
SMTP_HOST = "lifestoryapp-com.mail.protection.outlook.com"
EMAILS_FROM_EMAIL = "account@lifestoryapp.com"
EMAILS_FROM_NAME = "Lifestory"

def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> None:
    assert EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(EMAILS_FROM_NAME, EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": SMTP_HOST, "port": SMTP_PORT}
    if SMTP_TLS:
        smtp_options["tls"] = True
    environment_parsed = {k: v if v else '' for k, v in environment.items()}
    response = message.send(to=email_to, render=environment_parsed, smtp=smtp_options)
    logging.info(f"send email result: {response}")

def send_test_email(email_to: str) -> None:
    subject = "LIFESTORY TEST - Test email"
    with open(Path("./app/mailing/email_templates") / "test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": "LIFESTORY TEST", "email": email_to},
    )

def send_email_administrator(content: str) -> None:
    subject = "LIFESTORY - Warning"
    template_name = "admin.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to="dev@keysource.be",
        subject_template=subject,
        html_template=template_str,
        environment={"content": content},
    )

def send_register_confimation(user: schemas.User) -> None:
    subject = "LIFESTORY - Account created"
    template_name = "account_registered_en.html"
    if (user.lang.lower() == "fr") :
        subject = "LIFESTORY - Compte créé"
        template_name  = "account_registered_fr.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to=user.email,
        subject_template=subject,
        html_template=template_str,
        environment={"name": user.name},
    )

def send_reset_password_email(user: schemas.User, token: str) -> None:
    subject = "LIFESTORY - Reset Password"
    template_name = "reset_password_en.html"
    if (user.lang.lower() == "fr") :
        subject = "LIFESTORY - Réinitialisation du mot de passe"
        template_name  = "reset_password_fr.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to=user.email,
        subject_template=subject,
        html_template=template_str,
        environment={"name": user.name, "token": token },
    )

def send_password_update(user: schemas.User) -> None:
    subject = "LIFESTORY - Your password has been changed"
    template_name = "confirmation_password_reset_en.html"
    if (user.lang.lower() == "fr") :
        subject = "LIFESTORY - Votre mot de passe a été changé"
        template_name  = "confirmation_password_reset_fr.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to=user.email,
        subject_template=subject,
        html_template=template_str,
        environment={"name": user.name},
    )

def send_mfa_code(user: schemas.User, mfa_code: str, email: str) -> None:
    subject = "LIFESTORY - MFA authorization"
    template_name = "mfa_code_en.html"
    if (user.lang.lower() == "fr") :
        subject = "LIFESTORY - Autorisation MFA"
        template_name  = "mfa_code_fr.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to=email,
        subject_template=subject,
        html_template=template_str,
        environment={"name": user.name, "mfa_code": str(mfa_code).zfill(6)},
    )


def send_account_deletion_mfa_code(user: schemas.User, mfa_code: str, email: str) -> None:
    subject = "LIFESTORY - Your authorization for account deletion"
    template_name = "deletion_account_code_en.html"
    if (user.lang.lower() == "fr") :
        subject = "LIFESTORY - Votre autorisation pour la suppression de compte"
        template_name  = "deletion_account_code_fr.html"
    with open(Path("./app/mailing/email_templates") / template_name, encoding="utf-8") as f:
        template_str = f.read()
    send_email(
        email_to=email,
        subject_template=subject,
        html_template=template_str,
        environment={"name": user.first_name, "mfa_code": str(mfa_code).zfill(6)},
    )
