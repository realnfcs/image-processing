import { Link } from 'react-router-dom'

import './SideBar.css'

const sidebarData = [

  {
    title: "Início",
    path: "/",
  },

  {
    title: "Operações Algébricas",
    path: "/algebraic",
  },

  {
    title: "Transformações de Intensidade",
    path: "/intensity-transformations",
  },

  {
    title: "Operações em Histogramas",
    path: "/histogram",
  },

  {
    title: "Controle de Contraste Adaptativo",
    path: "/adaptive-contrast",
  },

  {
    title: "Transformações Geométricas",
    path: "/geometric",
  },

  {
    title: "Filtros",
    path: "/filters",
  },

  {
    title: "Detecção de Bordas",
    path: "/edge-detectention",
  },

  {
    title: "Aguçamento de Bordas",
    path: "/sharpening",
  },

  {
    title: "Convolução",
    path: "/convolution",
  },
]

function SideBar() {
  return (
    <div className="sidebar-container">
      <aside>
        <ul>
         {sidebarData.map((item, index) => {
            return (
              <li key={index} className="sidebar-items">
                <Link to={item.path}>
                  <span>{item.title}</span>
                </Link>
              </li>
            )
         })}
        </ul>
      </aside>
    </div>
  )
}

export default SideBar
