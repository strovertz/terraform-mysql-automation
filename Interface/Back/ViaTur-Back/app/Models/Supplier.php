<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Supplier extends Model
{
    use HasFactory;

    public $table = 'fornecedores';
    protected $primaryKey = 'id';
    protected $fillable = ['data','price','description','address','selectedOption'];
    public $guarded = ['update_at','created_at','id'];
}
