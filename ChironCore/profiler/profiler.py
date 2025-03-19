import time
import psutil
import os
from collections import defaultdict

class Profiler:
    def __init__(self):
        self.instruction_counts = defaultdict(int)
        self.instruction_times = defaultdict(float)
        self.variable_accesses = defaultdict(int)
        self.memory_usage = []
        self.start_time = None
        self.process = psutil.Process(os.getpid())
        
    def start_profiling(self):
        """Start profiling session"""
        self.start_time = time.time()
        self.instruction_counts.clear()
        self.instruction_times.clear()
        self.variable_accesses.clear()
        self.memory_usage.clear()
        
    def end_profiling(self):
        """End profiling session and return results"""
        end_time = time.time()
        total_time = end_time - self.start_time
        
        return {
            'total_time': total_time,
            'instruction_counts': dict(self.instruction_counts),
            'instruction_times': dict(self.instruction_times),
            'variable_accesses': dict(self.variable_accesses),
            'memory_usage': self.memory_usage
        }
    
    def track_instruction(self, instruction_type, execution_time):
        """Track instruction execution"""
        self.instruction_counts[instruction_type] += 1
        self.instruction_times[instruction_type] += execution_time
        
    def track_variable_access(self, variable_name):
        """Track variable access"""
        self.variable_accesses[variable_name] += 1
        
    def track_memory(self):
        """Track current memory usage"""
        self.memory_usage.append(self.process.memory_info().rss)
        
    def get_report(self):
        """Generate a human-readable profiling report"""
        report = []
        report.append("=== Chiron Profiling Report ===\n")
        
        # Instruction statistics
        report.append("Instruction Statistics:")
        for instr, count in self.instruction_counts.items():
            total_time = self.instruction_times[instr]
            avg_time = total_time / count if count > 0 else 0
            report.append(f"  {instr}:")
            report.append(f"    Count: {count}")
            report.append(f"    Total Time: {total_time:.4f}s")
            report.append(f"    Average Time: {avg_time:.4f}s")
        
        # Variable access statistics
        report.append("\nVariable Access Statistics:")
        for var, count in self.variable_accesses.items():
            report.append(f"  {var}: {count} accesses")
        
        # Memory statistics
        if self.memory_usage:
            report.append("\nMemory Statistics:")
            report.append(f"  Peak Memory: {max(self.memory_usage) / 1024 / 1024:.2f} MB")
            report.append(f"  Average Memory: {sum(self.memory_usage) / len(self.memory_usage) / 1024 / 1024:.2f} MB")
        
        return "\n".join(report) 