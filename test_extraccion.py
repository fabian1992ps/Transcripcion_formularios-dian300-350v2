"""Script de prueba para validar la extracción de los PDFs de ejemplo."""
import pdfplumber
import sys
sys.path.insert(0, '.')
from app import (
    extraer_cabecera_350, extraer_valores_350,
    extraer_cabecera_300, extraer_valores_300,
    limpiar_valor
)

def test_350():
    print("=" * 80)
    print("TEST FORMULARIO 350 - RETENCIÓN EN LA FUENTE")
    print("=" * 80)
    
    with pdfplumber.open(r"Formularios de ejemplo\Ejemplo formulario 350 retencion.pdf") as pdf:
        page = pdf.pages[0]
        words = page.extract_words(keep_blank_chars=True, x_tolerance=3, y_tolerance=3)
        
        # Test cabecera
        cab = extraer_cabecera_350(words)
        print(f"\nCabecera:")
        for k, v in cab.items():
            print(f"  {k}: {v}")
        
        # Test valores
        filas = extraer_valores_350(words)
        print(f"\nFilas de valores encontradas: {len(filas)}")
        print(f"\nDetalle por fila (top Y → valores):")
        
        conceptos = [
            "Rentas de trabajo", "Rentas de pensiones",
            "Honorarios", "Comisiones", "Servicios",
            "Rend. financieros", "Arrendamientos",
            "Regalías", "Dividendos", "Compras",
            "Tarjetas débito/crédito", "Contratos construcción",
            "Enajenación activos PN",
            "Loterías/rifas", "Hidrocarburos",
            "Otros pagos retención",
            "Pagos ext sin convenio", "Pagos ext con convenio",
            "Autoret Exonerados", "Autoret Ventas",
            "Autoret Honorarios", "Autoret Comisiones",
            "Autoret Servicios", "Autoret Rend Fin",
            "Autoret 65", "Autoret 66", "Autoret Otros",
        ]
        
        tops_sorted = sorted(filas.keys())
        
        # Separar multicol y solo-col4
        tops_multi = [t for t in tops_sorted if len(filas[t]) > 1 or "col1" in filas[t] or "col2" in filas[t] or "col3" in filas[t]]
        tops_single = [t for t in tops_sorted if t not in tops_multi]
        
        print(f"\n  Filas multicol ({len(tops_multi)}):")
        for i, t in enumerate(tops_multi):
            vals = filas[t]
            concepto = conceptos[i] if i < len(conceptos) else f"[#{i}]"
            parts = []
            for col in ["col1", "col2", "col3", "col4"]:
                v = vals.get(col, "")
                parts.append(f"{col}={v:>15}" if v != "" else f"{col}={'':>15}")
            print(f"    top={t:6} → {concepto:30} | {' | '.join(parts)}")
        
        print(f"\n  Filas solo-col4 ({len(tops_single)}):")
        totales_nombres = [
            "Menos ret exceso Renta", "Total ret renta",
            "Ret IVA responsables", "Ret IVA no residentes",
            "Menos ret IVA exceso", "Total ret IVA", "Timbre",
            "Total retenciones", "Sanciones", "Total ret + sanc"
        ]
        for i, t in enumerate(tops_single):
            vals = filas[t]
            nombre = totales_nombres[i] if i < len(totales_nombres) else f"[#{i}]"
            v4 = vals.get("col4", "")
            print(f"    top={t:6} → {nombre:30} | col4={v4:>15}")


def test_300():
    print("\n" + "=" * 80)
    print("TEST FORMULARIO 300 - IVA")
    print("=" * 80)
    
    with pdfplumber.open(r"Formularios de ejemplo\Ejemplo formulario 300 IVA.pdf") as pdf:
        page = pdf.pages[0]
        words = page.extract_words(keep_blank_chars=True, x_tolerance=3, y_tolerance=3)
        
        # Test cabecera
        cab = extraer_cabecera_300(words)
        print(f"\nCabecera:")
        for k, v in cab.items():
            print(f"  {k}: {v}")
        
        # Test valores
        casillas = extraer_valores_300(words)
        print(f"\nCasillas encontradas: {len(casillas)}")
        
        # Valores esperados del PDF (verificación manual):
        esperados = {
            "27": 0,        # gravados 5%
            "28": 258184000,  # gravados tarifa general
            "40": 95213000,   # no gravadas
            "41": 353397000,  # total ingresos brutos
            "43": 353397000,  # total ingresos netos
            "51": 24829000,   # import bienes tarifa gral
            "53": 111276000,  # import servicios tarifa gral
            "54": 227073000,  # excluidos exentos
            "55": 363178000,  # total compras brutas
            "57": 363178000,  # total compras netas
            "59": 49055000,   # IVA generado tarifa gral
            "67": 49055000,   # total impuesto generado
            "72": 4718000,    # imp desc compras bienes gral
            "75": 14175000,   # imp desc servicios gral
            "77": 18893000,   # total impuesto pagado/facturado
            "81": 18893000,   # total descontables
            "82": 30162000,   # saldo a pagar período
            "86": 30162000,   # saldo a pagar impuesto
            "88": 30162000,   # total saldo a pagar
        }
        
        print(f"\nVerificación contra valores esperados:")
        ok = 0
        fail = 0
        for cas, esperado in esperados.items():
            real = casillas.get(cas, "NO ENCONTRADO")
            match = "✅" if real == esperado else "❌"
            if real == esperado:
                ok += 1
            else:
                fail += 1
            print(f"  {match} Casilla {cas:>3}: esperado={esperado:>15,.0f} | real={real if isinstance(real, str) else f'{real:>15,.0f}'}")
        
        print(f"\n  Resultado: {ok} OK, {fail} FALLOS de {len(esperados)} verificados")
        
        print(f"\nTodas las casillas extraídas:")
        from app import F300_CONCEPTOS
        for cas in sorted(casillas.keys(), key=lambda x: int(x)):
            nombre = F300_CONCEPTOS.get(cas, "???")
            val = casillas[cas]
            print(f"  Casilla {cas:>3} = {val:>15,.0f}  ({nombre})")


if __name__ == "__main__":
    test_350()
    test_300()
