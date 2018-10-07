import h5py
import numpy as np
from ROOT import TFile

f=TFile('ArCube_0000.root')
argon=f.Get('argon')

file=h5py.File('ArCube_0000.hdf5','w')
g1=file.create_group('incoming_neutrino')
g2=file.create_group('primary_interaction')
g3=file.create_group('4D_charge_distribution')

incoming_variables=['pida','xa','ya','za','ta','pxa','pya','pza','ekina','ma']

primary_interactions=['pidi', 'xi','yi','zi','pyi','ti','pzi','ekini','mi']

charge_dist_vars=['tidq','pidq','sidq','dq','xq','yq','zq']

for a1 in incoming_variables:
    array=np.zeros(1000)
    var=eval('argon.'+ a1)
    for b1 in range(1000):
        argon.GetEntry(b1)
        array[b1]=var
    g1.create_dataset(a1,data=array)

ni_array=np.zeros(1000,dtype=int)
for a2 in range(argon.GetEntries()):
    argon.GetEntry(a2)
    ni_array[a2]=int(argon.ni)
g2.create_dataset('ni',data=ni_array)

max_ni=np.max(ni_array)
for a3 in primary_interactions:
    array2=np.full((1000,max_ni),np.nan)
    for b3 in range(1000):
        argon.GetEntry(b3)
        var2=eval('argon.'+ a3)
        for c1 in range(ni_array[b3]):
            array2[b3][c1]=var2[c1]
    g2.create_dataset(a3,data=array2)

nq_array=np.zeros(1000,dtype=int)
for a4 in range(argon.GetEntries()):
    argon.GetEntry(a4)
    nq_array[a4]=argon.nq
g2.create_dataset('nq',data=nq_array)

max_nq=np.max(nq_array)
for a5 in charge_dist_vars:
    array3=np.full((1000,max_nq),np.nan)
    for b5 in range(argon.GetEntries()):
        argon.GetEntry(b5)
        var3=eval('argon.'+ a5)
        for c2 in range(nq_array[b5]):
            array3[b5][c2]=var3[c2]
    g3.create_dataset(a5,data=array2)

file.close()
    
