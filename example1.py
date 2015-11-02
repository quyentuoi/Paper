__author__ = 'quyen'
from fnss import *

topo = dumbbell_topology(5, 4)
# topo = parse_rocketfuel_isp_map("file.cch")
C = [1, 10, 40]
set_capacities_edge_betweenness(topo, C, 'Gbps')
set_weights_inverse_capacity(topo)
set_delays_constant(topo, 2, 'ms')
set_buffer_sizes_bw_delay_prod(topo)

tm = sin_cyclostationary_traffic_matrix(
topo, mean=0.5, stddev=0.05,
gamma=0.8, log_psi=-0.33, delta=0.2,
n=24, periods=7, max_u=0.9
)


write_topology(topo, 'topology.xml')
write_traffic_matrix(tm, 'traffic-matrix.xml')