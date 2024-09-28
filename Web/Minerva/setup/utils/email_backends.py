# from django.core.mail import get_connection, send_mail
# from django.core.mail.backends.smtp import EmailBackend
# class MultipleSMTPBackend(EmailBackend):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.backends = [
#             {
#                 'EMAIL_HOST': 'smtp.gmail.com',
#                 'EMAIL_PORT': 587,
#                 'EMAIL_HOST_USER': 'minervaembv@gmail.com',
#                 'EMAIL_HOST_PASSWORD': 'a u z q y d f v a w a x m o h a',
#                 'EMAIL_USE_TLS': True
#             },
#             {
#                 'EMAIL_HOST': 'smtp.outlook.com',
#                 'EMAIL_PORT': 587,
#                 'EMAIL_HOST_USER': 'minervaembv@gmail.com',
#                 'EMAIL_HOST_PASSWORD': 'a u z q y d f v a w a x m o h a',
#                 'EMAIL_USE_TLS': True
#             },
#             # Adicione mais servidores aqui
#         ]

#     def send_messages(self, email_messages):
#         for backend_config in self.backends:
#             try:
#                 # Cria uma conexão para cada backend
#                 connection = get_connection(
#                     backend='django.core.mail.backends.smtp.EmailBackend',
#                     **backend_config
#                 )
#                 connection.send_messages(email_messages)
#                 return len(email_messages)  # Se tiver sucesso, interrompe o loop
#             except Exception as e:
#                 # Se falhar, tenta o próximo backend
#                 continue
#         return 0  # Se nenhum backend conseguir enviar, retorna 0