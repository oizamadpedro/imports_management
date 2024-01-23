import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function ClientSells({ clientSells }){
    return (
        <TableContainer component={Paper}>
            <Table aria-label="simple table" className='tableSell'>
                <TableHead>
                <TableRow>
                    <TableCell align="right"><b>Produto</b></TableCell>
                    <TableCell align="right"><b>Valor</b></TableCell>
                    <TableCell align="right"><b>Lucro</b></TableCell>
                </TableRow>
                </TableHead>
                <TableBody>
                {clientSells.map((sell) => (
                    <TableRow
                    key={sell.sell_id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                    >
                    <TableCell align="right"><b>{sell.product}</b></TableCell>
                    <TableCell align="right"><b style={{ color: 'green' }}>R${sell.price}</b></TableCell>
                    <TableCell align="right"><b style={{ color: '#6574FF' }}>R${Math.round(sell.profit * 1000) / 1000}</b></TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
        </TableContainer>
    )

}