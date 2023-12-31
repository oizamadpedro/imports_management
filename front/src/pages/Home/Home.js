import MUITable from '../../components/MUITable/MUITable';
import './home.css';
import { useEffect, useState } from 'react';

export default function Home() {

    const [sells, setSells] = useState([]);

    useEffect(() => {
        const fetchSells = async () => {
          try {
            const response = await fetch("http://localhost:8000/v1/sells/");
            if (!response.ok) {
              throw new Error(`Erro na requisição: ${response.status}`);
            }
            const sellsData = await response.json();
            console.log(sellsData.data);
            setSells(sellsData.data);
          } catch (error) {
            console.error("Erro ao buscar dados:", error);
            // Trate o erro, se necessário
          }
        };
    
        fetchSells();
    }, []);

    return(
        <div id="home">
            <h1>OSIO Software</h1>
            <p>Confira as ultimas vendas abaixo</p>
            <br /> <br/>
            <div id="lastSell">
                <MUITable sells={sells} />
            </div>
        </div>
    )
}