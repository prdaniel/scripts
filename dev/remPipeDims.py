
def remDims(dimLine):
    pipeFile = "C:/Endeca/apps/Discover/config/pipeline/Discover.dimension_refs.xml"
    pipeFileTmp = pipeFile+".tmp"
    shutil.copy2(pipeFile, pipeFileTmp)
    dim_refs = open(pipeFile, "r")
    lines = dim_refs.readlines()
    dim_refs.close()
    dim_refs_out = open(pipeFile, "w")
    for line in lines:
        if 'NAME="'+dimLine+'"' not in line:
            dim_refs_out.write(line)
    dim_refs_out.close    
    
remDims("trigger.page_type")
            