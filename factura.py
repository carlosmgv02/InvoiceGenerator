#!/usr/bin/env python3
import os
import sys
import argparse

from customers import customers, billing_info
from tempfile import NamedTemporaryFile
from datetime import datetime

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from file_manager import create_invoice_path

# Configurar el idioma de la factura
os.environ["INVOICE_LANG"] = "es"
def parse_date(date_string):
    """Convierte una cadena de texto en un objeto de fecha."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        msg = "No es un formato de fecha válido: '{0}'. El formato debe ser YYYY-MM-DD.".format(date_string)
        raise argparse.ArgumentTypeError(msg)
# Definir la configuración de los argumentos esperados
parser = argparse.ArgumentParser(description="Generar una factura en PDF.")
parser.add_argument('--customer', type=str, help='Nombre del cliente, debe estar en el diccionario de customers.')
parser.add_argument('--hours', type=float, help='Número de horas trabajadas.')
parser.add_argument('--rate', type=float, help='Tarifa por hora (opcional, si no se proporciona se usa la tarifa del cliente).')
parser.add_argument('--num_factura', type=str, help='Número de factura.')
parser.add_argument('--fecha', type=parse_date, help='Fecha de la factura en formato YYYY-MM-DD.')

args = parser.parse_args()

# Verificar si el cliente existe en el diccionario de customers
if args.customer and args.customer in customers:
    customer = customers[args.customer]
else:
    print("Cliente no encontrado. Asegúrese de que el nombre del cliente esté correctamente en el diccionario de customers.")
    sys.exit()

client = Client(customer['name'], ir=customer['cif'], address=customer['address'])
provider = Provider(billing_info['name'], address=billing_info['address'], ir=billing_info['nif'], bank_account=billing_info['iban'])
creator = Creator('John Doe')

# IRPF e IVA
irpf = 15
iva = 21

invoice = Invoice(client, provider, creator, irpf_rate=irpf, iva_rate=iva, date=args.fecha)
invoice.currency = u'€'
invoice.number = args.num_factura  # Número de factura

hourly_rate = args.rate if args.rate else customer['hourly_rate']

# Agregar las horas trabajadas como un ítem en la factura
invoice.add_item(Item(args.hours, hourly_rate, description=customer['service'], tax=21))

base_path = '/path/to/invoices'
invoice_path = create_invoice_path(base_path, args.customer, args.fecha)
pdf_filename = os.path.join(invoice_path, f'Factura_{args.customer.upper()}_{args.num_factura}.pdf')

pdf = SimpleInvoice(invoice)
pdf.gen(pdf_filename)

print(f"Factura generada y guardada en: {pdf_filename}")
response = input("¿Quieres abrir la factura? (Pulsa Enter para abrir, cualquier otra tecla para salir): ")
if response == '':
    os.system(f"open '{invoice_path}'")
