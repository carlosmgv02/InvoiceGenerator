import os
from datetime import date


def get_trimester(month):
    """Devuelve el trimestre basado en el mes."""
    if 1 <= month <= 3:
        return '1r trim'
    elif 4 <= month <= 6:
        return '2º trim'
    elif 7 <= month <= 9:
        return '3r trim'
    elif 10 <= month <= 12:
        return '4º trim'
    else:
        raise ValueError("Mes inválido")


def get_month_name(month):
    """Devuelve el nombre del mes en español basado en el número del mes."""
    months = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo',
        4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
        10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    return months.get(month, None)


def create_invoice_path(base_path, client_name, invoice_date):
    """Crea el camino completo para guardar la factura y crea las carpetas si no existen."""
    month = invoice_date.month
    year = invoice_date.year
    trimester = get_trimester(month)
    month_name = get_month_name(month)

    # Construir la ruta completa
    path = os.path.join(base_path, str(year), trimester, 'Ingresos', month_name, client_name)

    # Crear la carpeta si no existe
    os.makedirs(path, exist_ok=True)

    return path
