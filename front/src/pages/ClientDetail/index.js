import { useEffect, useState } from 'react';
import './index.css';
import { useParams } from 'react-router-dom';
import { getApi } from '../../utils/fetchapi';
import  clientPerfil  from '../../assets/img/perfil.png';

export default function Client(){

    const { id } = useParams();
    const [client, setClient] = useState([]);

    useEffect(() => {
        const getClient = async () => {
          const data = await getApi(`http://localhost:8000/v1/clients/${id}`);
          setClient(data);
        }
        getClient();
      }, []);   
    
    

    return (
        <div id='client-detail-page'>
            <div id='client-detail-container'>
                <div id='client-perfil'>
                    <img src={clientPerfil} alt='perfil do cliente' />
                </div>
                {client?.map((client) => (
                    <h1>{client.counterpart_name}</h1>
                ))}
            </div>
        </div>
    )
}