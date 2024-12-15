nip=['']
nm =['']
gol=['']
jk=[0]
data_pegawai=[]
adl='y';
x=0;
while (adl=='y') or (adl=='Y'):
    nip[x]=input('NIP :')
    nip.append('')
    nm[x] =input('Nama :')
    nm.append('')
    gol[x]=input('Golongan :')
    gol.append('')
    jk[x] =input('Jam Kerja:')
    jk.append('')
    x=x+1;
    data_pegawai.append({
        'NIP': nip,
        'Nama': nm,
        'Golongan': gol,
        'Jam Kerja': jk
    })
    adl =input('Ada Data Lagi[Y/T]:')
    
print('Entry Data Pegawai')
print('==================')



print('Laporan Data Pegawai')
print('==============================================================================================')
print('| No|      NIP       |          NAMA         | GOL | G.POKOK | J.KERJA | G.LEMBUR | T.GAJI| ')
print('==============================================================================================')

tgs=0;
for i, pegawai in enumerate(data_pegawai): 
    if gol[i]=='A':
        gp=1000000
    elif gol[i]=='B':
        gp=1500000
    elif gol[i]=='C':
        gp=2000000
    else :
        gp=2500000

    if int(jk[i])>160:
        gl=(int(jk[i])-160)*10000
    else:
        gl=0

tg=gp+gl
tgs=gl+tg
print('|',i+1,'|',nip[i],'|',nm[i],'|',gol[i],'  |',gp,'| ',jk[i],'  | ',gl,'|',tg,'|');  

print('==============================================================================================')

print('Total Gaji Keseluruhan :'+str(tgs));