import { useEffect, useState } from 'react';
import './add.css';
import { TextField, Button, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
export default function Add(){
    const [data, setData] = useState({
        product_id: '',
        price: '',
        rate_product: '',
        shop: '',
        buy_date: '',
        quantity: '',
        order_id: '',
    });
    const [products, setProducts] = useState()
    const [productId, setProductId] = useState()

    const handleChange = (event) => {
        setData({ ...data, product_id: event.target.value })
    };
    
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

    const adicionaCompra = (e) => {
        e.preventDefault();
        console.log(data);
        console.log("aaddd");
        fetch('http://localhost:8000/v1/buyProducts/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json',
            },
        })
        .then((resp) => resp.json())
        .catch((err) => {
            console.log(err)
        })
    }

    return(
        <div id="add_page">
            <div id="add_container">
                <div id="add_title">
                    <h3>Adicionar Compra</h3>
                </div>
                <br />
                <div id="add_buy">
                    <form onSubmit={adicionaCompra} id="buy_form">
                        <div className='form-row'>
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Produto</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={productId}
                                label="Produto"
                                onChange={handleChange}
                                required
                            >
                                {products?.map((product) => (
                                    <MenuItem value={product.id}>{product.product}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        </div>
                        <div className="form-row">

                        </div>
                        <div className="form-row">
                            <TextField
                                name="price"
                                label="Price"
                                variant="outlined"
                                required
                                value={data.price}
                                onChange={(e) => setData({ ...data, price: e.target.value })}
                            />
                            <TextField
                                name="rate_product"
                                label="Rate Product"
                                variant="outlined"
                                value={data.rate_product}
                                required
                                onChange={(e) => setData({ ...data, rate_product: e.target.value })}
                            />
                        </div>
                        <div className="form-row">
                            <TextField
                                name="shop"
                                label="Shop"
                                required
                                variant="outlined"
                                value={data.shop}
                                onChange={(e) => setData({ ...data, shop: e.target.value })}
                                fullWidth
                            />
                        </div>
                        <div className="form-row">
                            <TextField
                                name="quantity"
                                label="Quantity"
                                required
                                variant="outlined"
                                value={data.quantity}
                                onChange={(e) => setData({ ...data, quantity: e.target.value })}
                            />
                            <TextField
                                name="order_id"
                                label="Order ID"
                                required
                                variant="outlined"
                                value={data.order_id}
                                onChange={(e) => setData({ ...data, order_id: e.target.value })}
                            />
                        </div>
                        <div className="form-row">
                            <Button type="submit" variant="contained" color="primary">
                                Adicionar Compra
                            </Button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}