# Invoice Generator

This Python script facilitates the generation of PDF invoices based on worked hours and other specific client data. It's designed to automate the creation of invoices for different clients, storing the generated documents in an organized structure based on the date and client.
## Features
- Generation of invoices in PDF format.
- Configuration of client and provider data via command line arguments.
- Automatic storage of generated invoices in a directory structure based on date and client.
- Easy configuration of invoice language.
## Requirements
- Python 3.x 
- External libraries: `InvoiceGenerator`, `argparse`, `datetime`
- Predefined client data and billing configuration.
## Installation 
1. Clone the repository or download the necessary files. 
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
``` 
3. Ensure that client data and billing configuration are correctly set up in `customers.py` and `billing_info.py` modules.
## Usage

The script is run from the command line, providing several necessary arguments for generating the invoice:

```bash
python factura.py --customer <CustomerName> --hours <WorkedHours> --num_factura <InvoiceNumber> --fecha <InvoiceDate> [--rate <HourlyRate>]
```


### Arguments 
- `--customer`: The name of the client, which must match an entry in the client dictionary. 
- `--hours`: Number of hours worked. 
- `--rate`: Hourly rate. This argument is optional if the client has a predefined rate. 
- `--num_factura`: Invoice number. 
- `--fecha`: Invoice date in the format `YYYY-MM-DD`.
### Example Usage

```bash
python factura.py --customer "Customer1" --hours 34.5 --num_factura "2024-001-AC" --fecha "2024-01-15"
```