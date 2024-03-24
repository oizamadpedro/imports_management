import './header.css';
import logo from '../../assets/img/osio_black.png';
import { Button } from '@mui/material';
export default function Header(){
    const logout = () => {
        localStorage.setItem('jwt', "");
    }
    return (
        <div id='header'>
            <div>
                <img src={logo} alt='logo' />
            </div>
            <div></div>
            <div>
                <a href="/login"><Button variant='outlined' onClick={() => logout()} >Logout</Button></a>
                <a href="/">HOME</a>
            </div>
        </div>
    )
}