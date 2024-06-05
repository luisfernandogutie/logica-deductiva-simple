import sys
sys.path.append('..')

from src.logic import elegible

def main():
    estudiantes = ['Juan', 'María', 'Pedro']
    for estudiante in estudiantes:
        if elegible(estudiante):
            print(f"{estudiante} es elegible para recibir una beca.")
        else:
            print(f"{estudiante} no es elegible para recibir una beca.")

if __name__ == "__main__":
    main()