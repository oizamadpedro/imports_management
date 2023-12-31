import './home.css';
import { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

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
    
    const columns = [
        { field: 'id', headerName: 'ID', width: 70 },
        { field: 'price', headerName: 'Price', width: 130 },
        { field: 'product', headerName: 'Product', width: 130 },
        { field: 'counterpart_name', headerName: 'Name', width: 130 },
        { field: 'cel_number', headerName: 'Number', width: 130 },
    ]
    return(
        <div id="home">
            <h1>OSIO Software</h1>
            <p>Confira as ultimas vendas abaixo</p>
            <br /> <br/>
            <div id="lastSell">
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell align="right">Produto</TableCell>
                            <TableCell align="right">Valor</TableCell>
                            <TableCell align="right">Nome</TableCell>
                            <TableCell align="right">Número de Celular</TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                            {sells.map((sell) => (
                                <TableRow
                                key={sell.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell align="right">{sell.product}</TableCell>
                                <TableCell align="right">R${sell.price}</TableCell>
                                <TableCell align="right">{sell.counterpart_name}</TableCell>
                                <TableCell align="right">{sell.cel_number}</TableCell>
                                
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </div>
    )
}