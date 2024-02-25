![alt text](Financial_Management_Banner.png)
# Funcionalidad de Cálculo de Intereses

Este módulo extiende las capacidades del sistema para calcular y aplicar intereses sobre facturas pendientes, permitiendo a las empresas gestionar de manera eficiente los intereses por pagos atrasados.

## Características

- Cálculo automático de intereses basado en condiciones predefinidas.
- Configuración flexible de tasas de interés y periodos de gracia.
- Integración con el módulo de facturación para una gestión unificada.

## Requisitos

- Odoo 15.0 o superior.
- Módulo de Contabilidad o Facturación de Odoo instalado y configurado.

## Instalación

Para instalar este módulo, sigue los siguientes pasos:

1. Copia el módulo en tu carpeta de addons de Odoo.
2. Actualiza la lista de aplicaciones dentro de Odoo.
3. Busca "Cálculo de Intereses" en la lista de aplicaciones y haz clic en instalar.

## Configuración

### Configuración de Períodos de Tasa de Interés

1. Navega a Contabilidad > Configuración > Períodos de Tasa de Interés.
2. Crea un nuevo registro con los detalles del período y la tasa de interés.

### Configuración de Reglas de Interés

1. Navega a Contabilidad > Configuración > Reglas de Interés.
2. Crea una nueva regla definiendo la condición bajo la cual se aplicará la tasa de interés.

## Uso

Una vez configurado el módulo, el sistema calculará automáticamente los intereses en las facturas pendientes basándose en las reglas definidas. Los intereses se calcularán y mostrarán como líneas adicionales en las facturas correspondientes.

## Desarrollo

### Extender Funcionalidades

Para extender o modificar este módulo, revisa el código fuente y considera las dependencias con otros módulos de Odoo.

### Correr Pruebas

Para asegurar la calidad del módulo, se incluyen pruebas unitarias. Ejecútalas utilizando el comando:

```sh
./odoo-bin -d tu_base_de_datos --test-enable --log-level=test --stop-after-init -i interest
```

## Soporte

Si encuentras un bug o necesitas soporte, por favor crea un issue en el sistema de seguimiento de issues de este proyecto. 

## Contacto
### Correo Electrónico

dmunoztech@gmail.com

### Teléfono

+505 5829 4839



