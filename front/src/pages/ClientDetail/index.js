import { useEffect, useState } from 'react';
import './index.css';
import { useParams } from 'react-router-dom';
import { getApi, getAuthApi } from '../../utils/fetchapi';
import  clientPerfil  from '../../assets/img/perfil.png';
import whatsapp from '../../assets/img/whatsapp.png';
import ClientSells from '../../components/ClientSell';
import { getToken } from '../../utils/auth';


export default function Client(){

    const { id } = useParams();
    const [client, setClient] = useState([]);
    const [sells, setSells] = useState([]);

    useEffect(() => {
        const getClient = async () => {
          const data = await getAuthApi(`/v1/clients/${id}`, getToken());
          setClient(data.data);
        }
        const getClientSells = async () => {
            const data = await getAuthApi(`/v1/clients/sells/${id}`, getToken())
            setSells(data.data);
        }
        getClient();
        getClientSells();
      }, [id]);
    
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
                <ClientSells clientSells={sells} />
            </div>
          </div>
        </div>
      );      
}