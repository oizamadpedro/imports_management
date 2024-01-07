import './clients.css';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useEffect, useState } from 'react';
import { Button } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import TransitionModal from '../../components/Modal';

export default function Clients(){

    const [clients, setClients] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/v1/clients")
            .then((response) => response.json())
            .then((json) => {
                setClients(json.results);
            })
    }, []);
 
    return(
        <div id='clients'>
            <h1>OSIO Software</h1>
            <p>Todos os clientes cadastrados</p>
            <div id="clientsTable">
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell align="left"><b>ID</b></TableCell>
                            <TableCell align="left"><b>Nome</b></TableCell>
                            <TableCell align="left"><b>Documento</b></TableCell>
                            <TableCell align="left"><b>CEP</b></TableCell>
                            <TableCell align="left"><b>Telefone</b></TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                            {clients?.map((client) => (
                                <TableRow
                                key={client.id}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell align="left"><b style={{color: "rgb(98, 98, 254)"}}>{client.client_id}</b></TableCell>
                                <TableCell align="left"><b style={{color: "rgb(98, 98, 254)"}}>{client.counterpart_name}</b></TableCell>
                                <TableCell align="left"><b>{client.document}</b></TableCell>
                                <TableCell align="left"><b>{client.cep}</b></TableCell>
                                <TableCell align="left"><b>{client.cel_number}</b></TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
            <div id="buttonClient">
                <TransitionModal />

            </div>
        </div>
    )
}

