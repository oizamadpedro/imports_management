import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function MUITable(props){
    return(
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
                    {props.sells.map((sell) => (
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
    )
}