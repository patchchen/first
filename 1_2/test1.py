
import first.serial_initial as serial_initial , first.serial_read_write as serial_read_write , first.serial_release as serial_release




from first.tcp_initial import tcp_init
from first.tcp_read_write import tcp_read, tcp_write
from first.tcp_release import tcp_release

connection = tcp_init("127.0.0.1", 5000)

tcp_write(connection, "Hello")
data = tcp_read(connection)

tcp_release(connection)

