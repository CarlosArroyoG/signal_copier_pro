function SignalForm() {
    const [signal, setSignal] = useState('');
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        await api.createSignal({ content: signal });
        setSignal('');
        alert('Signal created successfully');
      } catch (error) {
        console.error('Error creating signal:', error);
        alert('Failed to create signal');
      }
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <textarea
          value={signal}
          onChange={(e) => setSignal(e.target.value)}
          placeholder="Enter your trading signal here"
          required
        />
        <button type="submit">Send Signal</button>
      </form>
    );
  }
  
  export default SignalForm;