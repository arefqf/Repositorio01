from abc import ABC, abstractmethod
# Clase Documentación
class Documentación:
    def __init__(self):
        self.documentos = []
    def agregar_documento(self, documento):
        self.documentos.append(documento)
    def imprimir_documento(self):
        return "\n".join(self.documentos)
# Interfaz builder
class ConstructorDocumentaciónVehículo(ABC):
    @abstractmethod
    def construye_solicitud_pedido(self):
        pass
    @abstractmethod
    def construye_solicitud_matriculación(self):
        pass
    @abstractmethod
    def obtener_documentación(self):
        pass
# Constructor concreto 1
class ConstructorDocumentaciónVehículoHtml(ConstructorDocumentaciónVehículo):
    def __init__(self):
        self.documentación = Documentación()
    def construye_solicitud_pedido(self):
        self.documentación.agregar_documento("Solicitud de pedido en formato HTML")
    def construye_solicitud_matriculación(self):
        self.documentación.agregar_documento("Solicitud de matriculación en formato HTML")
    def obtener_documentación(self):
        return self.documentación.imprimir_documento()

# Constructor concreto 2
class ConstructorDocumentaciónVehículoPdf(ConstructorDocumentaciónVehículo):
    def __init__(self):
        self.documentación = Documentación()
    def construye_solicitud_pedido(self):
        self.documentación.agregar_documento("Solicitud de pedido en formato PDF")
    def construye_solicitud_matriculación(self):
        self.documentación.agregar_documento("Solicitud de matriculación en formato PDF")
    def obtener_documentación(self):
        return self.documentación.imprimir_documento()

# Clase Director
class Vendedor:
    def hacer_documentacion(self, constructor):
        constructor.construye_solicitud_pedido()
        constructor.construye_solicitud_matriculación()

# Documentacion html
print("Documentos en html:")
director_vendedor = Vendedor()
documentacion_vehiculo_html = ConstructorDocumentaciónVehículoHtml()
director_vendedor.hacer_documentacion(documentacion_vehiculo_html)
documento_html = documentacion_vehiculo_html.obtener_documentación()
print(documento_html)
print("")
print("Documentos en pdf:")
# Documentacion html
director_vendedor = Vendedor()
documentacion_vehiculo_pdf = ConstructorDocumentaciónVehículoPdf()
director_vendedor.hacer_documentacion(documentacion_vehiculo_pdf)
documento_pdf = documentacion_vehiculo_pdf.obtener_documentación()
print(documento_pdf)