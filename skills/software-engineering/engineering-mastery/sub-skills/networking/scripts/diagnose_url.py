from urllib.parse import urlparse
import socket, ssl, sys

def diagnose(url):
    u=urlparse(url if '://' in url else 'https://'+url)
    host=u.hostname; port=u.port or (443 if u.scheme=='https' else 80)
    ip=socket.gethostbyname(host)
    sock=socket.create_connection((host, port), timeout=5)
    tls=False
    if u.scheme=='https':
        ctx=ssl.create_default_context(); sock=ctx.wrap_socket(sock, server_hostname=host); tls=True
    sock.close()
    return {'host':host,'port':port,'ip':ip,'tcp_connect':True,'tls':tls}
if __name__ == '__main__':
    print('PASS networking diagnosis', diagnose(sys.argv[1] if len(sys.argv)>1 else 'https://example.com'))
