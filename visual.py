from hello import Graph
import hello as gen
from pyvis.network import Network

g=Graph()
e=g.edges()
pat=gen.listazapat
e1=[x[0] for x in e]
e2=[x[1] for x in e]

e=e1+e2
e=list(dict.fromkeys(e))

E1=[]
for i in e1:
    E1.append(str(i))
E2=[]
for i in e2:
    E2.append(str(i))
E=[]
for i in e:
    E.append(str(i))
PAT=[]
for i in pat:
    PAT.append(str(i))
water_net = Network(height="1080px", width="1920px", font_color="black")

w = [1 for i in range(len(E1))]

edge_data = zip(E1, E2, w)
print(PAT)
PAT.reverse()

print(PAT)
if len(PAT):
    prvo = PAT.pop()
    if len(PAT):
        vtoro = PAT.pop()

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    print(src + " " + prvo)
    print(dst + " " + vtoro)

    if src==prvo and dst==vtoro and len(PAT)!=0:
        print("sdg")
        water_net.add_node(src, src, title=src, color="#00ff1e")
        water_net.add_node(dst, dst, title=dst, color="#00ff1e")
        water_net.add_edge(src, dst, value=w, color="#00ff1e")
        if len(PAT):
            prvo = PAT.pop()
            if len(PAT):
                vtoro = PAT.pop()

    else:
        water_net.add_node(src, src, title=src)
        water_net.add_node(dst, dst, title=dst)
        water_net.add_edge(src, dst, value=w)

neighbor_map = water_net.get_adj_list()

for node in water_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

water_net.show("mygraph.html")