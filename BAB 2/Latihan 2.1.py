import ModulePythonPertamaku
ModulePythonPertamaku.ucapkanSalam()
print(ModulePythonPertamaku.kuadratkan(5))
print(ModulePythonPertamaku.buah)
print('------------------------------------------')
import ModulePythonPertamaku as mpp
mpp.ucapkanSalam()
print(mpp.daftarBaju)
print(mpp.jumlahBaju)
print('------------------------------------------')
from ModulePythonPertamaku import kuadratkan, daftarBaju
print(kuadratkan(6))
print(daftarBaju)
print('------------------------------------------')
from ModulePythonPertamaku import ucapkanSalam as ucap
ucap()