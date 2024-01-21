import { useEffect, useState } from 'react';
import './index.css';
import { useParams } from 'react-router-dom';
import { getApi } from '../../utils/fetchapi';
import  clientPerfil  from '../../assets/img/perfil.png';
import whatsapp from '../../assets/img/whatsapp.png';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function Client(){

    const { id } = useParams();
    const [client, setClient] = useState([]);
    const [sells, setSells] = useState([]);

    useEffect(() => {
        const getClient = async () => {
          const data = await getApi(`http://localhost:8000/v1/clients/${id}`);
          setClient(data);
        }
        const getClientSells = async () => {
            const data = await getApi(`http://localhost:8000/v1/clients/sells/${id}`)
            setSells(data);
        }
        getClient();
        getClientSells();
      }, []);   
    
    console.log(client);
    
    function mappedAddress(address){
        address = JSON.parse(address)
        let endereco = "";
        endereco += `${address.logradouro} - ${address.bairro} - ${address.localidade}/${address.uf}`
        console.log(endereco);
        return endereco
    }

    return (
        <div id='client-detail-page'>
          <div id='client-detail-container'>
            <div id='client-perfil'>
              <img src={clientPerfil} alt='perfil do cliente' />
            </div>
            {client?.map((client) => (
              <div key={client.id}>
                <div id='client-name'>
                  <h1>{client.counterpart_name}</h1>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', marginTop: '10px' }}>
                  <img src={whatsapp} alt='whatsapp icon' style={{ width: '25px', marginRight: '5px' }} />
                  <p>{client.cel_number}</p>
                </div>
                <div>
                    <p>{client.document? (
                        <p><b>Documento</b> {client.document}</p>
                    ): null}</p>
                    {client.address_json ? (
                        <p>
                            <b>Endereço:</b> {mappedAddress(client.address_json)} {client.cep}
                        </p>
                    ) : null}
                </div>
                {/* Adicione aqui os outros elementos dentro do mapeamento */}
              </div>
            ))}
            <br></br>
            <div id='client-buy-history'>
                <h3>Histórico de Compras</h3>
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
                        {sells.map((sell) => (
                            <TableRow
                            key={sell.sell_id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <TableCell align="right"><b>{sell.product}</b></TableCell>
                            <TableCell align="right"><b style={{ color: 'green' }}>R${sell.price}</b></TableCell>
                            <TableCell align="right"><b style={{ color: '#6574FF' }}>{Math.round(sell.profit * 1000) / 1000}</b></TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
          </div>
        </div>
      );      
}