
import nbformat as nbf
import os
#%%

## Set important paths
BASE = os.getcwd()
INPUT_PATH=os.path.join(BASE,'input py file')
OUTPUT_PATH=os.path.join(BASE,'output ipynb file')

print(BASE)
#%%

# =============================================================================
# example
# =============================================================================
nb = nbf.v4.new_notebook()

#%%

text1 = """\
# My first automatic Jupyter Notebook
This is an auto-generated notebook."""

code1 = """\
%pylab inline
hist(normal(size=2000), bins=50)"""

text2 = """\
# My first automatic Jupyter Notebook
This is an auto-generated notebook."""

code2 = """\
%pylab inline
hist(normal(size=2000), bins=50)"""


nb['cells'] = [nbf.v4.new_markdown_cell(text1),nbf.v4.new_code_cell(code1), nbf.v4.new_markdown_cell(text2),nbf.v4.new_code_cell(code2)]

#%%

nbf.write(nb, OUTPUT_PATH+'\\test.ipynb')

# =============================================================================
# end example
# =============================================================================

#%%
def get_documentsDOC(path=INPUT_PATH):
    for name in os.listdir(path):
        if name.endswith('.py') and 'py_to_nb' not in name:
            yield os.path.join(path, name),name[:-3]

#%% 
            
# Print the total number of documents
print('Total number of documnets to convert: ' , len(list(get_documentsDOC(INPUT_PATH))))
#%%

def dcouments_to_cells(filetext):
        file_text_cells=filetext.split('#%%') 
        return file_text_cells


#%%
        
def convert_into_format(file_text_cells):
    li=[]
    for c in file_text_cells:
        li.append(nbf.v4.new_code_cell(c))
    return li

#%%
def create_documents_cells(docs_input=INPUT_PATH,docs_output=OUTPUT_PATH):
    for path,name in get_documentsDOC(docs_input):
        with open(path,encoding='utf-8') as file: 
            filetext=file.read()
            file_text_cells = dcouments_to_cells(filetext)
            li_cells=convert_into_format(file_text_cells)
            nb = nbf.v4.new_notebook()
            nb['cells']=li_cells
            newpath=os.path.join(docs_output,name)+'.ipynb'
            nbf.write(nb, newpath)
            print(newpath)



#%%

create_documents_cells()




