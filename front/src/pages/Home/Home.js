import { Button } from '@mui/material';
import MUITable from '../../components/MUITable/MUITable';
import './home.css';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import { TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import { getApi, postApi } from '../../utils/fetchapi';
import CloseIcon from '@mui/icons-material/Close';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function Home() {
    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [profit, setProfit] = useState(false);
    const [products, setProducts] = useState([]);
    const [clients, setClients] = useState([]);
    const [sells, setSells] = useState([]);
    const [buys, setBuys] = useState([]);
    const [isAdd, setIsAdd] = useState(false);
    const [clientId, setClientId] = useState("")
    const [buysId, setBuysId] = useState("")
    const [productId, setProductId] = useState("")
    const [data, setData] = useState({
      product_id: '',
      client_id: '',
      buy_id: '',
      price: '',
      sell_date: ''
    });

    const limpaCamposDeAddDaVenda = () => {
      document.getElementById('produto').value = "";
      document.getElementById('cliente').value = "";
      document.getElementById('compra').value = "";
      document.getElementById('preco').value = "";
      document.getElementById('venda').value = "";
    }

    const changeProductId = (event) => {
      setProductId(event.target.value);
      setData({ ...data, product_id: event.target.value })
    };
    const changeClientId = (event) => {
      setClientId(event.target.value);
      setData({ ...data, client_id: event.target.value })
    };
    const changeBuyId = (event) => {
      setBuysId(event.target.value);
      setData({ ...data, buy_id: event.target.value })
    };

    const adicionaVenda = async (e) => {
      e.preventDefault();
      limpaCamposDeAddDaVenda()
      const responseVenda = await postApi('http://localhost:8000/v1/sellProducts/', data)
      console.log(responseVenda);
    }

    useEffect(() => {
      const findProducts = async () => {
        const data = await getApi("http://localhost:8000/v1/products");
        setProducts(data);
      }
      const fetchSells = async () => {
        const data = await getApi("http://localhost:8000/v1/sellProfit/");
        setSells(data);
      }
      const allClients = async () => {
        const data = await getApi("http://localhost:8000/v1/clients/");
        setClients(data);
      }
      const allBuys = async () => {
        const data = await getApi("http://localhost:8000/v1/buys/");
        setBuys(data);
      }
      findProducts();
      fetchSells();
      allClients();
      allBuys();
    }, []);   

    return(
        <div id="home">
            <h1>OSIO Software</h1>
            <p>Confira as ultimas vendas abaixo</p>
            <br /> <br/>
            <div id="lastSell">
              <MUITable sells={sells} profit={profit}/>
            </div>
            <div id="lucro">
              <Button variant="outlined" onClick={handleOpen}><AddIcon />Adicionar</Button>
              <Modal
                aria-labelledby="transition-modal-title"
                aria-describedby="transition-modal-description"
                open={open}
                onClose={handleClose}
                closeAfterTransition
                slots={{ backdrop: Backdrop }}
                slotProps={{
                  backdrop: {
                    timeout: 500,
                  },
                }}
              >
                <Fade in={open}>
                  <Box sx={style}>
                    <form onSubmit={adicionaVenda} id="buy_form">
                        <Button variant='outlined' onClick={() => setOpen(false)}><CloseIcon  /> Fechar</Button>
                        <div className="form-row">
                            <FormControl fullWidth>
                                <InputLabel id="demo-simple-select-label">Produto</InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="produto"
                                    value={productId}
                                    label="Produto"
                                    onChange={changeProductId}
                                    required
                                >
                                  {products?.map((product) => (
                                    <MenuItem value={product.id}>{product.product}</MenuItem>
                                  ))}
                                </Select>
                            </FormControl>
                        </div>
                        <div className="form-row">
                          <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Cliente</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="cliente"
                                value={clientId}
                                label="Cliente"
                                onChange={changeClientId}
                                required
                            >
                              {clients?.map((client) => (
                                <MenuItem value={client.client_id}>{client.counterpart_name}</MenuItem>
                              ))}
                            </Select>
                          </FormControl>
                        </div>
                        <div className="form-row">
                          <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Compra</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="compra"
                                value={buysId}
                                label="Compras"
                                onChange={changeBuyId}
                                required
                            >
                              {buys?.map((buy) => (
                                <MenuItem value={buy.id}>{buy.product} - {buy.quantity}</MenuItem>
                              ))}
                            </Select>
                          </FormControl>
                        </div>
                        <div className="form-row">
                          <TextField
                            name="price"
                            id="preco"
                            label="Preço"
                            variant="outlined"
                            required
                            value={data.price}
                            onChange={(e) => setData({ ...data, price: e.target.value })}
                            fullWidth
                          />
                          <TextField
                            name="sell_date"
                            id="venda"
                            label="Data de Venda"
                            variant="outlined"
                            required
                            value={data.sell_date}
                            onChange={(e) => setData({ ...data, sell_date: e.target.value })}
                            fullWidth
                          />
                        </div>
                        <div className="form-row">
                          <Button type="submit" variant="contained" color="primary" onClick={() => setIsAdd(true)}>
                            Adicionar Venda
                          </Button>
                          <Collapse in={isAdd}>
                            <Alert severity="success">Venda adicionada com sucesso</Alert>
                          </Collapse>
                          
                        </div>
                    </form>
                  </Box>
                </Fade>
              </Modal>
              <Button variant='contained' onClick={() => setProfit(!profit)}>{profit ? 'Ocultar Lucro' : 'Mostrar Lucro'}</Button>
            </div>
            <div id="border"></div>
            <div id="linkTable">
              <Link to="/compras"><Button variant='contained'>Tabela de Compras</Button></Link>
              <Link to="/products"><Button variant='contained'>Catálogo de Produtos</Button></Link>
              <Link to="/clients"><Button variant='contained'>Clientes Cadastrados</Button></Link>
              <Link to="/dashboard"><Button variant='contained'>Dashboard</Button></Link>
            </div>
        </div>
    )
}