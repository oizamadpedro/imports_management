import { Button } from '@mui/material';
import MUITable from '../../components/MUITable/MUITable';
import './home.css';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
    const [profit, setProfit] = useState(false);
    const [sells, setSells] = useState([]);

    useEffect(() => {
        const fetchSells = async () => {
          try {
            const response = await fetch("http://localhost:8000/v1/sellProfit/");
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
              <MUITable sells={sells} profit={profit}/>
            </div>
            <div id="lucro">
              <Button variant='outlined'>Adicionar Venda</Button>
              <Button variant='contained' onClick={() => setProfit(!profit)}>{profit ? 'Ocultar Lucro' : 'Mostrar Lucro'}</Button>
            </div>
            <div id="border"></div>
            <div id="linkTable">
              <Link to="/compras"><Button variant='contained'>Tabela de Compras</Button></Link>
              <Link to="/products"><Button variant='contained'>Catálogo de Produtos</Button></Link>
              <Link to="/clients"><Button variant='contained'>Clientes Cadastrados</Button></Link>
            </div>
        </div>
    )
}