import json
import os
import hashlib

blockchain_dir=os.curdir+'/blockchain/'

def get_hash(filename):
    file = open(blockchain_dir+filename,'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files ])

def check_integrity():
    files = get_files()
    results =[]
    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']
        prev_file = str(file -1)
        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'
        results.append({'block':prev_file,'result':res})
    return results
def write_block(name,amount,to,prev_hash=''):
    files=get_files()
    prev_file=files[-1]
    filename=str(prev_file+1)
    prev_hash=get_hash(str(prev_file))
    data ={"name":name,
            'amount':amount,
            'to':to,
            'hash':prev_hash}
    with open(blockchain_dir + filename,'w') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
def main():
    #write_block(name='oleg',amount='5',to='ksusha')
    print(check_integrity())

if __name__ == '__main__':
    main()

# d48dc9b0d5e5f94635a06eaf7ed6623e80f12e66e2eafd24755bce0188f48d52
# 9c57085e8a81212e5019c3c478c77391dfe55b8f18642b469fde90fa4a5e8e1e