def SortSBT(SBTfile,n=99999):
    '''
    Sort the Non-synonymous mutation data according to the position order
    '''
    num = n
    sbt = open(SBTfile,'r').read().split('\n')   # input Non-synonymous mutation data
    while '' in sbt:
        sbt.remove('')                           # remove empty element in sbt （list）
    SBTs=[]
    for i in range(num):                         # Sorting procedure
        for line in sbt:
            pos = int(line.split('\t')[0][1:][:-1])
            if pos == int(i):
                SBTs.append(line)
    return SBTs                                  # return sorted Non-synonymous mutation list

def read_SNP_pos_info(SNP_pos_info):
    '''
    Enter the base position on reference sequence (DNA) information
    '''
    snp=open(SNP_pos_info,'r').read().split('\n')[1:]
    while '' in snp:
        snp.remove('')
    return snp

def Getting_NSM_signature(SBTfile,Base_pos_idx,OTPT):
    '''
    creation of NSM signature
    '''
    write_in = open(OTPT,'a',encoding="utf-8")
    SNP_info=read_SNP_pos_info(Base_pos_idx)  #list
    SBT_info=SortSBT(SBTfile)          #list
    for i in range(len(SBT_info)):
        sbt_pos=SBT_info[i].split('\t')[0][1:][:-1]   # getting amino acide position of substitution
        for j in range(len(SNP_info)):
            ref_pos=SNP_info[j].split('\t')[5]   # getting amino acide position of reference protein sequence
            if sbt_pos==ref_pos and SNP_info[j-1].split('\t')[5] != ref_pos:  
                sbt_mark=''
                cnt=0
                for line in SNP_info[j-3:j+6]:
                    cnt+=1
                    if cnt < 4:
                        sbt_mark+=line.split('\t')[3]
                    elif cnt == 4:
                        sbt_mark+=str(SBT_info[i].split('\t')[1].split(r'>')[1])
                    elif cnt >=7:
                        sbt_mark+=line.split('\t')[3]
                print(r'>'+SBT_info[i].split('\t')[0]+'\n'+sbt_mark,file=write_in)
    write_in.close()

if __name__ == "__main__":
    Getting_NSM_signature(r'PATH\Substitution_in_POOL1andPOOL2.tab',
                          r'PATH\DNA_Base_info.txt',
                          r'PATH\NSM_signature.fasta')