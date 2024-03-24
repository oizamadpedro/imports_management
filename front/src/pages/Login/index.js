import './index.css';
import { useEffect, useState } from 'react';
import { Input, TextField, Button, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import { getApi, postApi } from '../../utils/fetchapi';
import { useNavigate } from "react-router-dom";
import Alert from '@mui/material/Alert';

export default function Login(){

    const [token, setToken] = useState();
    const [submitedLogin, setSubmitedLogin] = useState();
    const [userData, setUserData] = useState({
        "email": "",
        "password": ""
    });

    const navigate = useNavigate(); 

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };

    const authenticateUser = async (e) => {
        setSubmitedLogin(true);
        e.preventDefault();
        const dataToken = await postApi("/auth/v1/login", userData);
        console.log(dataToken);
        const jwtToken = dataToken['token'];
        if (jwtToken) {
            setToken(jwtToken);
            localStorage.setItem("jwt", jwtToken);
        } else {
            
        }
    }

    useEffect(() => {
        if (token && submitedLogin) {
            navigate('/');
        }
    }, [token, submitedLogin, navigate]);

    return (
        <div id="login-page">
            <div id="login-container">
                <h1>Login</h1>
                <form onSubmit={authenticateUser}>
                    <div className='form-row'>
                        <TextField
                            name="email"
                            label="Email"
                            variant="outlined"
                            required
                            onChange={handleChange}
                            style={{width: '100%'}}
                            value={userData.email}
                        />
                    </div>
                    <div className='form-row'>
                        <TextField
                            name="password"
                            label="Senha"
                            variant="outlined"
                            required
                            style={{width: '100%'}}
                            onChange={handleChange}
                            type='password'
                            value={userData.password}
                        />
                    </div>
                    <div className="form-row">
                        <Button type="submit" variant="contained" color="primary" style={{width: '100%'}}>
                            Logar
                        </Button>
                        { (token && submitedLogin) && <Alert severity="success">Autenticado com sucesso.</Alert>}
                        { (!token && submitedLogin) && <Alert severity="error">Alguma informação está errada.</Alert>}
                        
                    </div>
                </form>
                <div className='form-row' style={{margin: '10px'}}>
                    <p>Ainda não tem um cadastro? <a href="/register" style={{textDecoration: 'none'}}>Cadastre-se aqui</a></p>
                </div>
            </div>
        </div>
    )
}