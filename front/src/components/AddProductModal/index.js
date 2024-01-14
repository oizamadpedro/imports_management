import { Button } from '@mui/material';
import MUITable from '../../components/MUITable/MUITable';
import IconButton from '@mui/material/IconButton';
import { useEffect, useState } from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import { TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import CloseIcon from '@mui/icons-material/Close';
import { postApi } from '../../utils/fetchapi';


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
export default function AddProduct(){
    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [isAdd, setIsAdd] = useState(false);
    const [data, setData] = useState({
        product: '',
        quantity: 0,
        description: ''
    });

    const adicionaProduto = (e) => {
        e.preventDefault();
        const responseVenda = postApi('http://localhost:8000/v1/products/', data)
        console.log(responseVenda);
        setOpen(false)
    }

    return (
        <div>
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
                <form onSubmit={adicionaProduto}>
                    <IconButton onClick={() => setOpen(false)}>
                        <CloseIcon  />
                    </IconButton>
                    <div className="form-row">
                        <TextField
                            name="product"
                            id="product"
                            label="Produto"
                            variant="outlined"
                            required
                            onChange={(e) => setData({ ...data, product: e.target.value })}
                            fullWidth
                        />
                    </div>
                    <div className="form-row">
                        <TextField
                        name="description"
                        id="description"
                        label="Descrição"
                        variant="outlined"
                        required
                        value={data.description}
                        onChange={(e) => setData({ ...data, description: e.target.value })}
                        fullWidth
                        />
                    </div>
                    <div className="form-row">
                        <Button type="submit" variant="contained" color="primary" onClick={() => setIsAdd(true)}>
                        Adicionar Produto
                        </Button>
                        <Collapse in={isAdd}>
                        <Alert severity="success">Produto adicionado com sucesso</Alert>
                        </Collapse>
                    </div>
                </form>
                </Box>
            </Fade>
            </Modal>
        </div>
    )
}