import './header.css';
import logo from '../../assets/img/osio_black.png';

export default function Header(){
    return (
        <div id='header'>
            <div>
                <img src={logo} alt='logo' />
            </div>
            <div></div>
            <div>
                <a href="/">HOME</a>
            </div>
        </div>
    )
}