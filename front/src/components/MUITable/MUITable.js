import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Link } from 'react-router-dom';
import './index.css';

export default function MUITable(props){
    return(
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table" className='tableSell'>
                <TableHead>
                <TableRow>
                    <TableCell align="right"><b>Produto</b></TableCell>
                    <TableCell align="right"><b>Valor</b></TableCell>
                    {props.profit && <TableCell align="right"><b>Lucro</b></TableCell>}
                    <TableCell align="right"><b>Nome</b></TableCell>
                    <TableCell align="right"><b>Número de Celular</b></TableCell>
                </TableRow>
                </TableHead>
                <TableBody>
                {props.sells.map((sell) => (
                    <TableRow
                    key={sell.sell_id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                    >
                    <TableCell align="right"><b>{sell.product}</b></TableCell>
                    <TableCell align="right"><b style={{ color: 'green' }}>R${sell.price}</b></TableCell>
                    {props.profit && <TableCell align="right"><b style={{ color: 'green' }}>R${sell.profit}</b></TableCell>}
                    <TableCell align="right"><Link to={"/client/" + sell.client_id}>{sell.counterpart_name}</Link></TableCell>
                    <TableCell align="right">{sell.cel_number}</TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}