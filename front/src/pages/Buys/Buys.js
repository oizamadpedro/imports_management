import './buys.css';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useEffect, useState } from 'react';
import { Button } from '@mui/material';
import { getAuthApi } from '../../utils/fetchapi';
import { getToken } from '../../utils/auth';

export default function Buys(){

    const [buys, setBuys] = useState([]);

    useEffect(() => {
      const getBuys = async () => {
        const data = await getAuthApi(`/v1/buys/`, getToken());
        console.log(data);
        setBuys(data.data);
      }
      getBuys();
    }, []);
    

    return(
        <div id="buys">
            <h1>OSIO Software</h1>
            <p>Tabela de Compras</p>
            <div id="buysTable">
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell align="left"><b>Ordem</b></TableCell>
                            <TableCell align="left"><b>Produto</b></TableCell>
                            <TableCell align="left"><b>Quantidade</b></TableCell>
                            <TableCell align="left"><b>Preço</b></TableCell>
                            <TableCell align="left"><b>Taxa</b></TableCell>
                            <TableCell align="left"><b>Loja</b></TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                        {buys.map((buy) => (
                            <TableRow
                            key={buy.id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <TableCell align="left"><b style={{color: "rgb(98, 98, 254)"}}>{buy.order_id}</b></TableCell>
                            <TableCell align="left"><b>{buy.product}</b></TableCell>
                            <TableCell align="left"><b>{buy.quantity}</b></TableCell>
                            <TableCell align="left"><b style={{color: "green"}}>R${buy.price}</b></TableCell>
                            <TableCell align="left">R${buy.rate_product}</TableCell>
                            <TableCell align="left">{buy.shop}</TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
            <div id="buyButton">
              <a href='/add'><Button variant='contained'>Adicionar Compra</Button></a>
            </div>
            <div id="border"></div>
        </div>
    )
}