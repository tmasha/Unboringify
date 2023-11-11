import React, {useState} from 'react';
import '../utils/navbar.css';
import logo from '../assets/logo.png';

const Menu = () => {
    return (
        <>
            <p><a href="/">Home</a></p>
            <p><a href="generate"><button type="button" className="generate-btn">Generate</button></a></p>
        </>
    );
};


const Navbar = () => {
    const [toggleMenu, setToggleMenu] = useState(false);

    return (
        <div className='navbar position-sticky'>

            {/*Subsections*/}
            <div className='navbar-links'>

            </div>
            {/*Logo*/}
            <div className='navbar-logo'>
                <a href='/'></a>
                <h1 id="logo">Unboringify</h1>
            </div>
            {/*Menu*/}
            <div className='navbar-menu'>
                <Menu />
            </div>
        </div>
    )
}

export default Navbar;