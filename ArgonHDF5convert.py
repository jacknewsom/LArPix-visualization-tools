import hdf5
import numpy as np
from ROOT import TFile

f=TFile('ArCube_0000.root')
argon=f.Get('argon')

file=h5py.file('ArCube_0000.hdf5','w')
g1=file.create_group('incoming_neutrino')
g2=file.create_group('primary_interaction')
g3=file.create_group('4D_charge_distribution')

incoming_variables=['pida','xa','ya','za','ta','pxa','pya','pza','ekina','ma']

primary_interactions=['pidi', 'xi' 'yi','zi','P','xi','pyi','pzi','ekini','mi']

charge_dist_vars=['tidq','pidq','sidq','dq','xq','yq','zq']

for a in incoming_variables:
    array=np.zeros(1000)
    var=eval('argon.'+a)
    for b in range(argon.GetEntries()):
        argon.GetEnty(b)
        array[b]=var
    g1.create_dataset(a,data=array)

ni_array=np.zeros(1000)
for a in range(argon.GetEntries()):
    argon.GetEntry(a)
    ni_array[a]=argon.ni
g2.create_dataset('ni',data=ni_array)

max_ni=np.max(ni_array)
for a in primary_interactions:
    array2=np.empty(1000,dtype=object)
    var2=eval('argon.'+a)
    for b in range(argon.GetEntries()):
        for c in range(ni_array[b]):
            argon.GetEntry(b)
            array2[b][c]=var2[c]
    g2.create_dataset(a,data=array2)

nq_array=np.zeros(1000)
for a in range(argon.GetEntries()):
    argon.GetEntry(a)
    nq_array[a]=argon.nq
g2.create_dataset('nq',data=nq_array)

max_nq=np.max(nq_array)
for a in charge_dist_vars:
    array3=np.empty(1000,dtype=object)
    var3=eval('argon.'+a)
    for b in range(argon.GetEntries()):
        for c in range(nq_array[b]):
            argon.GetEntry(b)
            array3[b][c]=var2[c]
    g3.create_dataset(a,data=array2)

file.close()
    
