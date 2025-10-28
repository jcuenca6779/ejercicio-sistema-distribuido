import time # Usaremos esto para añadir marcas de tiempo a los logs

class Nodo:
    """
    Representa un nodo en un sistema de archivos distribuido simple.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = {}
        
        # --- REQUISITO 1: Agregar un registro (log) a cada nodo ---
        # Inicializamos el log como una lista vacía
        self.log = []
        
        print(f"Nodo '{self.nombre}' inicializado.")

    def _registrar_accion(self, mensaje):
        """
        Método auxiliar privado para añadir entradas al log con formato.
        """
        # Obtenemos la hora actual para el registro
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_entry = f"[{timestamp}] {mensaje}"
        self.log.append(log_entry)

    def almacenar_archivo(self, nombre_archivo, contenido):
        """
        Almacena un archivo en el diccionario 'archivos' del nodo.
        """
        self.archivos[nombre_archivo] = contenido
        
        # --- REQUISITO 2: Registrar la acción de almacenamiento ---
        self._registrar_accion(f"ACCIÓN: Almacenado '{nombre_archivo}'")
        print(f"[{self.nombre}] Archivo '{nombre_archivo}' guardado.")

    def obtener_archivo(self, nombre_archivo):
        """
        Obtiene un archivo del diccionario 'archivos' del nodo.
        """
        contenido = self.archivos.get(nombre_archivo, None)
        
        # --- REQUISITO 2: Registrar la acción de recuperación ---
        if contenido is not None:
            self._registrar_accion(f"ACCIÓN: Recuperado '{nombre_archivo}'")
            print(f"[{self.nombre}] Archivo '{nombre_archivo}' recuperado.")
        else:
            # También registramos si el intento de recuperación falló
            self._registrar_accion(f"ACCIÓN: Intento fallido de recuperar '{nombre_archivo}'")
            print(f"[{self.nombre}] Archivo '{nombre_archivo}' no encontrado.")
            
        return contenido

    def mostrar_log(self):
        """
        --- REQUISITO 3: Muestra el log final de cada nodo ---
        """
        print(f"\n--- Log Final del Nodo: {self.nombre} ---")
        if not self.log:
            print("  (Sin entradas de log)")
        else:
            for entrada in self.log:
                print(f"  {entrada}")
        print("-" * (25 + len(self.nombre)))


# --- DEMOSTRACIÓN DE EJECUCIÓN ---
if __name__ == "__main__":
    
    print("Iniciando simulación del Sistema de Archivos...\n")
    
    # Creamos dos nodos
    nodo1 = Nodo(nombre="Servidor-Alpha")
    nodo2 = Nodo(nombre="Servidor-Beta")
    
    print("\n--- Realizando Operaciones ---")
    
    # Simulamos almacenamiento en ambos nodos
    nodo1.almacenar_archivo(nombre_archivo="config.ini", contenido="user=admin")
    nodo2.almacenar_archivo(nombre_archivo="datos.json", contenido="{'id': 123}")
    
    # Simulamos recuperación
    nodo1.obtener_archivo(nombre_archivo="config.ini")
    
    # Simulamos un intento fallido de recuperación
    nodo2.obtener_archivo(nombre_archivo="reporte.pdf") # Este archivo no existe
    
    print("\n--- Mostrando Logs Finales ---")
    
    # Mostramos los logs de cada nodo
    nodo1.mostrar_log()
    nodo2.mostrar_log()