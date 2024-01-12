import * as React from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import Button from '@mui/material/Button';
import { TextField, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import Typography from '@mui/material/Typography';
import AddIcon from '@mui/icons-material/Add';
import Alert from '@mui/material/Alert';
import IconButton from '@mui/material/IconButton';
import Collapse from '@mui/material/Collapse';
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

export default function TransitionModal() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const [clientIsAdd, setClientIsAdd] = React.useState(false);

    const [data, setData] = React.useState({
        counterpart_name: '',
        document: '',
        cep: '',
        cel_number: '',
    });

    const adiciona = (e) => {
        e.preventDefault();
        console.log(data);
        console.log("aaddd");
        fetch('http://localhost:8000/v1/clients/', {
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
            <form onSubmit={adiciona} id="buy_form">
                <div className="form-row">
                    <TextField
                        name="counterpart_name"
                        label="Nome"
                        variant="outlined"
                        fullWidth
                        required
                        value={data.counterpart_name}
                        onChange={(e) => setData({ ...data, counterpart_name: e.target.value })}
                    />
                    <TextField
                        name="document"
                        label="CPF/CNPJ"
                        fullWidth
                        variant="outlined"
                        value={data.document}
                        onChange={(e) => setData({ ...data, document: e.target.value })}
                    />
                </div>
                <div className="form-row">
                    <TextField
                        name="cep"
                        label="Cep"
                        required
                        variant="outlined"
                        value={data.cep}
                        onChange={(e) => setData({ ...data, cep: e.target.value })}
                        fullWidth
                    />
                </div>
                <div className="form-row">
                    <TextField
                        name="cel_number"
                        label="Número de Celular"
                        required
                        variant="outlined"
                        fullWidth
                        value={data.cel_number}
                        onChange={(e) => setData({ ...data, cel_number: e.target.value })}
                    />
                </div>
                <div className="form-row">
                  <Button type="submit" variant="contained" color="primary" onClick={() => setClientIsAdd(true)}>
                    Adicionar Cliente
                  </Button>
                  <Collapse in={clientIsAdd}>
                    <Alert severity="success">Cliente adicionado com sucesso!</Alert>
                  </Collapse>
                  
                </div>
            </form>
          </Box>
        </Fade>
      </Modal>
    </div>
  );
}