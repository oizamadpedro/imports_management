import './products.css';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useEffect, useState } from 'react';
import { Button } from '@mui/material';

export default function Products(){

    const [products, setProducts] = useState()

    useEffect(() => {
        const findProducts = async () => {
            try {
                const response = await fetch("http://localhost:8000/v1/products");
                if (!response.ok) {
                throw new Error(`Erro na requisição: ${response.status}`);
                }
                const products = await response.json();
                console.log(products.data);
                setProducts(products.data);
            } catch (error) {
                console.error("Erro ao buscar dados:", error);
                // Trate o erro, se necessário
            }
        }
        findProducts()
    }, []);   
    return(
        <div id="products">
            <h1>OSIO Software</h1>
            <p>Catálogo de Produtos</p>
            <div id="productsTable">
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell align="left"><b>ID</b></TableCell>
                            <TableCell align="left"><b>Produto</b></TableCell>
                            <TableCell align="left"><b>Quantidade</b></TableCell>
                            <TableCell align="left"><b>Descrição</b></TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                        {products?.map((product) => (
                            <TableRow
                            key={product.id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                            <TableCell align="left"><b style={{color: "rgb(98, 98, 254)"}}>{product.id}</b></TableCell>
                            <TableCell align="left"><b>{product.product}</b></TableCell>
                            <TableCell align="left"><b>{product.quantity}</b></TableCell>
                            <TableCell align="left"><b>{product.description}</b></TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
            <div id="productButton">
              <a href='/addproduct'><Button variant='contained'>Adicionar Produto</Button></a>
            </div>
            <div id="border"></div>
        </div>
    )
}