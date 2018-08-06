

"""
install clang-devel
install pip clang
"""

import clang.cindex

s = """
int fact( int n){
  return (n>1)? n*fact(n-1):1;
  }
"""
clang.cindex.Config.set_library_file("/usr/lib64/libclang.so")

idx = clang.cindex.Index.create()

tu = idx.parse('tmp.cpp', args=['-std=c++11'], unsaved_files=[('tmp.cpp', s)], options=0)

for t in tu.get_tokens(extent=tu.cursor.extent):
    print(t.kind)
