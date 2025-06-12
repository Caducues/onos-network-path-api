from mininet.topo import Topo

class CustomTopo(Topo):
    def build(self):
        # 3 anahtar (switch)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # 3 ana bilgisayar (host)
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # Ana bilgisayarları anahtarlara bağla
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)

        # Anahtarlar arası bağlantılar (mesela üçgen yapı)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s1)

topos = {'att': (lambda: CustomTopo())}
